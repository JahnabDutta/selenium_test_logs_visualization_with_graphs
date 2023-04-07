import React, {Component,useEffect,useState} from 'react';
import {
    Grid,Paper
} from '@mui/material';
import JsonView from 'react-json-view';
import backendUrl from '../backendUrl';
const url = backendUrl;

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
        //make a div such that it takes up the whole screen and does not overflow
        <div>
            <Grid container direction="row" spacing={2}>
                <Grid item xs={12}>
                    <h1>Raw Log</h1>
                </Grid>
                <Grid item xs={12}>
                    <Paper>
                        <JsonView src={rawData} />
                    </Paper>
                </Grid>
            </Grid>
        </div>
    )
}

export default RawLog;