import axios from '~/helpers/axios';

export default function (ctx) {
    if(process.server){
        axios.defaults.headers.common = {}
        Object.keys(ctx.req.headers).map((key)=>{
            axios.defaults.headers.common[key] = ctx.req.headers[key];
        });
    }
}
