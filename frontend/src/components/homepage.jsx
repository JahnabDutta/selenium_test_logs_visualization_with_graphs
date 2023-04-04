import React, { Component } from 'react';
import {
    Grid
} from '@mui/material';
import SideBar from './side-bar';
import {Line,Pie } from 'react-chartjs-2';
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";

Chart.register(CategoryScale);

const data = {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [
        {
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
        },
    ],
};
function Home() {
    return ( 
        <div>
            <Grid 
            container
            direction="row"
            >
                <Grid item xs={2}
                >
                    <SideBar />
                </Grid>
                <Grid item xs={10}>
                    <Line data={data} />
                </Grid>
            </Grid>
        </div>
        
    )
}
    

export default Home;