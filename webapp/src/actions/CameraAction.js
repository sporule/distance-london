import * as types from './ActionTypes';
import Resources from "../helpers/Resources";

export function loadCameraSuccess(cameras){
    return {type:types.LOAD_CAMERA_SUCCESS,cameras};
}

export function loadCamera(){
    let resources = new Resources();
    return function(dispatch){
        return resources.getCameras().then(cameras=>{
            if(cameras!=null&&cameras!==undefined){
                dispatch(loadCameraSuccess(cameras));
            }
        })
    }
}