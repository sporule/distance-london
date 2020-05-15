import React from "react";
import * as Ons from "react-onsenui";



class TabBar extends React.Component{
  constructor(props, context) {
    super(props, context);
    /*
    this.state = {
    };
    */
}

  render(){
    return (
      <Ons.Tabbar
      swipeable={false}
      position="bottom"
      renderTabs={this.props.renderTabs}
      />
    );
  }
}


export default TabBar;