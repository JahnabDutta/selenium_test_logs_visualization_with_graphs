import React, {Component,onEffect,useEffect,useState} from 'react';
import {Line,Bar } from 'react-chartjs-2';
import Chart from "chart.js/auto";
import {
    Grid,
     Box
} from '@mui/material';
import { CategoryScale } from "chart.js";
import backendUrl from '../backendUrl';
const url = backendUrl;



Chart.register(CategoryScale);

function StandardLog({standardLogType}) {


    function colourGenerator(){
        //generate random rgb colour
        const r = Math.floor(Math.random() * 256);
        const g = Math.floor(Math.random() * 256);
        const b = Math.floor(Math.random() * 256);
        const alpha = Math.random() * (1 - 0.5) + 0.5;
        const rgb = `rgba(${r},${g},${b},${alpha})`;
        return rgb;
    }

    

    function makeGraphData(data,standardLogType){
        if(standardLogType=== 'all'){
            const dates = Object.keys(data);
            const count = Object.values(data);

            const graphData = {
                labels: dates,
                datasets: [
                    {
                        label: 'Number of logs',
                        data: count,
                        fill: false,
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgba(255, 99, 132, 0.2)',
                    },
                ],
            };

            return graphData;

        }
        else{
            var datasets = [];
            const dates = Object.keys(data[Object.keys(data)[0]]);
            // map over the data
            Object.keys(data).map((key) => {
                // get the values for each key
                const dates = Object.keys(data[key]);
                const count = Object.values(data[key]);
  
                const dataset = {
                    label: key,
                    data: count,
                    fill: false,
                    backgroundColor: colourGenerator(),
                    borderColor: colourGenerator(),
                };
                datasets.push(dataset);
            });

            const graphData = {
                labels: dates,
                datasets: datasets,
            };
            return graphData;
        }
        
    }

    useEffect(() => {
        const requestOptions = {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        };
        const apiUrl = url + 'logs/' + standardLogType + '/';
        fetch(apiUrl, requestOptions)
            .then(response => response.json())
            .then(data =>{
                const graphData = makeGraphData(data,standardLogType);
                setGraphData(graphData);
            })
            .catch(error => console.log(error));

        

    }, [standardLogType]);

    const blankGraphData = {
        labels: [],
        datasets: [
            {
                label: 'Number of logs',
                data: [],
                fill: false,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgba(255, 99, 132, 0.2)',
            },
        ],
    };


    const [graphData,setGraphData] = useState(blankGraphData);

    



    return (
        <div>
            <Grid container direction="row" spacing={2}>
                <Grid item xs={12}>
                    <h1>{standardLogType}</h1>
                </Grid>
                <Grid item lg={6} sm={12}>
                    <Bar data={graphData} />
                </Grid>
                <Grid item lg={6} sm = {12}>
                    <Line data={graphData} />
                </Grid>
            </Grid>


        </div>
    )
}

export default StandardLog;