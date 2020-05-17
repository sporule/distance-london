import * as types from '../actions/ActionTypes';
import InitialState from "./InitialState";



export function cameras(state=InitialState.cameras,action){
    switch(action.type){
        //add new videos to the states
        case types.LOAD_CAMERA_SUCCESS:
            return action.cameras;
        default:
            return state;
    }
}