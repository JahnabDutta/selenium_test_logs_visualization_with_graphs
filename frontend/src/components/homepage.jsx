import React, { Component, useState, useEffect } from "react";
import { Grid } from "@mui/material";
import SideBar from "./side-bar";
import StandardLog from "./standard-log";
import Graph from "./graph";
import RawLog from "./raw-log";

function Home() {
  const [displayType, setDisplayType] = useState("welcome");
  const [standardLogType, setStandardLogType] = useState("none");
  const [graph, setGraph] = useState("none");
  const [rawLog, setRawLog] = useState("none");



  return (
    <div style={({ height: "100vh" }, { display: "flex"})}>
      
      
          <SideBar
            setDisplayType={setDisplayType}
            setStandardLogType={setStandardLogType}
            setGraph={setGraph}
            setRawLog={setRawLog}
          />
     
        <Grid container direction="row" margin={2} padding={2}>
        <Grid item xs={12}>
          {displayType === "welcome" && <h1>Welcome to the admin page</h1>}
          {displayType === "standard-log" && (
            <StandardLog standardLogType={standardLogType} />
          )}
          {displayType === "graph" && <Graph graph={graph} />}
          {displayType === "raw-log" && <RawLog rawLog={rawLog} />}
        </Grid>
      </Grid>
    </div>
  );
}

export default Home;
