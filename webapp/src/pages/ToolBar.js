﻿import React from "react";
import * as Ons from "react-onsenui";

class ToolBar extends React.Component{
  constructor(props, context) {
      super(props, context);
      this.popPage = this.popPage.bind(this);
  }

  popPage(){
    this.props.navigator.popPage();
  }


  render(){
    const backButton = this.props.route.props.hasBackButton
    ? <Ons.BackButton onClick={this.popPage}>Back</Ons.BackButton>
    : null;
    return(
      <Ons.Toolbar>
      <div className="left">{backButton}</div>
      <div className="center">
        {this.props.route.props.title}
      </div>
    </Ons.Toolbar>
  );
  }
}




export default ToolBar;