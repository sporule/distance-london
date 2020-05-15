﻿import React from "react";
import {RouteCreator} from "../helpers/General";
import Navigator from "./Navigator";
import MapPage from "./MapPage";

class MapTab extends React.Component {
  constructor(props, context) {
    super(props, context);
  }
    render() {
      //Initial Route for Video Tab
      const route = RouteCreator(MapPage,{title:"Map",hasBackButton:false});
      return (
        <Navigator route={route}/>
        );
    }
}

export default MapTab;