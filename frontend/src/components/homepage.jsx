import React, { Component, useState, useEffect } from "react";
import { Grid } from "@mui/material";
import SideBar from "./side-bar";
import StandardLog from "./standard-log";
import Graph from "./graph";
import RawLog from "./raw-log";

function Home() {
  const [displayType, setDisplayType] = useState("welcome");
  const [standardLogType, setStandardLogType] = useState("");
  const [graph, setGraph] = useState("");
  const [rawLog, setRawLog] = useState("");

  return (
    <div>
      <Grid container direction="row">
        <Grid item xs={2}>
          <SideBar
            setDisplayType={setDisplayType}
            setStandardLogType={setStandardLogType}
            setGraph={setGraph}
            setRawLog={setRawLog}
          />
        </Grid>
        <Grid item xs={10}>
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
