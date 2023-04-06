import React, {Component} from 'react';
import {Line,Pie } from 'react-chartjs-2';
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";

Chart.register(CategoryScale);


function Graph({graph}) {
    return (
        <div>
            <h1>Graph</h1>
        </div>
    )
}

export default Graph;