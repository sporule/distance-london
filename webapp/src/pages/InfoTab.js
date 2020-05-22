﻿import React from "react";
import {RouteCreator} from "../helpers/General";
import Navigator from "./Navigator";
import InfoPage from "./InfoPage";

class InfoTab extends React.Component {
  constructor(props, context) {
    super(props, context);
  }
    render() {
      //Initial Route for Video Tab
      const route = RouteCreator(InfoPage,{title:"Info",hasBackButton:false});
      return (
        <Navigator route={route}/>
        );
    }
}

export default InfoTab;