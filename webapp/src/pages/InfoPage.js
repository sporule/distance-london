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
          <p>As a starter data engineer, I wanted to help to build a safer London during this special time. Distance.London is my first project using AI detection technology to show users whether their destinations are crowded, in order to help users to keep social distance and stay safe.
</p>
          <p>Join us to Support NHS with the Social Distance AI, Distance.London at <a href="https://www.justgiving.com/fundraising/distance-london">Just Giving Fundraising</a>.</p>
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