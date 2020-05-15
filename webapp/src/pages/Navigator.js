import React from "react";
import * as Ons from "react-onsenui";
import ToolBar from "./ToolBar";


class Navigator extends React.Component{
    constructor(props, context) {
        super(props, context);
        this.state = {
        };
        this.renderPage = this.renderPage.bind(this);
    }

    renderToolBar(route,navigator){
        return(
            <ToolBar route={route} navigator={navigator}/>
        );
    }

    renderPage(route, navigator){
        //pass the navigator and props to the page
        //            <route.component props = {route.props} navigator = {navigator}/>
        route.props.navigator=navigator;
        return(
        <Ons.Page key={route.props.title} renderToolbar={this.renderToolBar.bind(this,route,navigator)}> 
            {React.createElement(route.component, route.props)}

        </Ons.Page>

        );
    }

    render() {
        return (
        <Ons.Navigator swipeable renderPage={this.renderPage} initialRoute={this.props.route}/>
        );
    }

}


export default Navigator;