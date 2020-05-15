import { combineReducers } from 'redux';
import {cameras} from './CameraReducer'

const rootReucer = combineReducers({
    cameras
});

export default rootReucer;