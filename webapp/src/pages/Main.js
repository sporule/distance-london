import React from "react";
import * as Ons from "react-onsenui";
import TabBar from "./TabBar";
import MapTab from "./MapTab";
import InfoTab from "./InfoTab";



class Main extends React.Component {
    constructor(props, context) {
        super(props, context);
        this.state = {
        };
    }

    render() {
        //setting up tabs
        const renderTabs = () => {
            return [
                {
                    content: <MapTab key={1} />,
                    tab: <Ons.Tab icon="md-layers" key={1} />
                },
                {
                    content: <InfoTab key={1} />,
                    tab: <Ons.Tab icon="md-info" key={2} />
                }

            ];
        };
        return (
            <div>
                <TabBar renderTabs={renderTabs} />
            </div>
        );
    }
}


export default Main;