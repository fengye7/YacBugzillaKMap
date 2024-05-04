import { API } from "@/utils/request"

export async function getKMapData() {
    try{
        const response = await API.get('/bugs/latest-bugs');
        return response.data;
    }catch(e){
        throw new Error('Error fetching KMap data'+ e.message);
    }
}