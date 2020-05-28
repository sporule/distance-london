import React from "react";
import * as Ons from 'react-onsenui';
import { connect } from "react-redux";


class InfoPage extends React.Component {
  constructor(props, context) {
    super(props, context);
  }

  componentDidMount() {

  }

  render() {
    return (
      <Ons.Page>
        <Ons.Card>
          <p>Distance.London is my first project using AI detection technology to show users whether their destinations are crowded, in order to help users to keep social distance and stay safe.</p>
        </Ons.Card>
      </Ons.Page>
    );
  }
}

function mapStateToProps(state) {
  return {
  };
}

export default connect(mapStateToProps)(InfoPage);