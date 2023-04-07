import React, {Component,useEffect,useState} from 'react';
import {
    Grid
} from '@mui/material';
const url = 'http://localhost:5000/';

function RawLog({rawLog}) {

    

    useEffect(() => {
        if(rawLog === 'none' || rawLog === undefined || rawLog === null || rawLog === ''){
            return;
        }
        const requestOptions = {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        };
        const apiUrl = url + 'logs/raw/' + rawLog + '/';
        console.log(apiUrl)
        fetch(apiUrl, requestOptions)
            .then(response => response.json())
            .then(data =>{
               
                setRawData(data);
            })
            .catch(error => console.log(error));

        

    }, [rawLog]);

    const [rawData,setRawData] = useState([]);
    
    return (
        <div>
            {rawData.map((log) => {
                return (
                    <Grid container>
                        <Grid item xs={12}>
                            <p>{log}</p>
                        </Grid>
                    </Grid>
                )
            })
            }
        </div>
    )
}

export default RawLog;