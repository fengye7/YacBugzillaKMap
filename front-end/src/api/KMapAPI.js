import { API } from "@/utils/request"
import axios from "axios";

export async function getLatestBugs() {
    try{
        const response = await API.get('/bugs/latest-bugs');
        return response.data;
    }catch(e){
        throw new Error('Error fetching KMap data'+ e.message);
    }
}

export const getKMapData = (domains) => {
    const params = new URLSearchParams();
    domains.forEach(domain => params.append('domains', domain));
    return axios.get(`http://127.0.0.1:8000/bugs/k-map-data?${params.toString()}`); // 数据量大，不用公共API设置（会超时）
  };
