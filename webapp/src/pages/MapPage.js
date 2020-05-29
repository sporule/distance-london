import React from "react";
import * as Ons from 'react-onsenui';
import { bindActionCreators } from 'redux';
import { connect } from "react-redux";
import { RouteCreator } from "../helpers/General";
import { Map, Marker, Popup, TileLayer, Circle } from 'react-leaflet'


class MapPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = { position: [51.51419, -0.08865] }
  }

  componentDidMount() {
    this.getCurrentPosition();
  }

  getCurrentPosition = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((p) => {
        this.setState({
          position: [p.coords.latitude, p.coords.longitude]
        });
      });
    } else {
      console.log("Geo Location not supported by browser");
    }
  }
  render() {
    return (
      <Ons.Page>
        <Map center={this.state.position} zoom="15" touchZoom={true}>
          <TileLayer
            attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Marker position={this.state.position}>
            <Popup>
              Your Current Location
          </Popup>
          </Marker>
          {
            this.props.cameras.map((camera, index) => {
              let videoLocation = "https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/" + camera.name + ".mp4";
              let color = "green";
              if (camera.count >= 5) {
                color = "yellow"
              }
              if (camera.count >= 10) {
                color = "red"
              }
              let liveCamera = (<video className="popup" autoPlay loop muted preload="metadata">
                <source src={videoLocation} type="video/mp4" />
              </video>)
              if (navigator.platform && /ipad|iphone|ipod/.test(navigator.platform.toLowerCase())) {
                liveCamera = (
                  <video className="popup" loop muted controls preload="metadata">
                    <source src={videoLocation} type="video/mp4" />
                  </video>
                )
              }
              return (
                <Circle key={index} center={camera.position} radius={150} color={color}>
                  <Popup>
                    <div>
                      <p>Pedestrian Count: {camera.count}</p>
                      <p>The number above was measured at {new Date(camera.update_time).toTimeString().slice(0, 8)}.</p>
                      <p>Please use live TFL Camera below to see the most recent situation:</p>
                      {liveCamera}
                    </div>
                  </Popup>
                </Circle>
              )
            })
          }
        </Map>
      </Ons.Page>
    );
  }
}

function mapStateToProps(state) {
  return {
    cameras: state.cameras,
    // sources:state.sources
  };
}

export default connect(mapStateToProps)(MapPage);