import React, { Component, useState } from "react";
import {
  Sidebar,
  Menu,
  MenuItem,
  useProSidebar,
  SubMenu,
} from "react-pro-sidebar";
import { TextField, Grid } from "@mui/material";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import NoteOutlinedIcon from "@mui/icons-material/NoteOutlined";
import FindInPageOutlinedIcon from "@mui/icons-material/FindInPageOutlined";
import SsidChartOutlinedIcon from "@mui/icons-material/SsidChartOutlined";
import TextSnippetOutlinedIcon from "@mui/icons-material/TextSnippetOutlined";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";

function SideBar({ setDisplayType, setStandardLogType, setGraph, setRawLog }) {
  const { collapseSidebar } = useProSidebar();
  const [graphtype, setGraphType] = useState("");
  const [rawlogtype, setRawLogType] = useState("");

  return (
    <div id="app" style={({ height: "100vh" }, { display: "flex" })}>
      <Sidebar style={{ height: "100vh" }}>
        <Menu>
          <MenuItem
            icon={<MenuOutlinedIcon />}
            onClick={() => {
              collapseSidebar();
            }}
            style={{ textAlign: "center" }}
          >
            {" "}
            <h2>Admin</h2>
          </MenuItem>

          <SubMenu icon={<TextSnippetOutlinedIcon />} label="Common logs">
            <MenuItem
              icon={<NoteOutlinedIcon />}
              onClick={() => {
                setDisplayType("standard-log");
                setStandardLogType("all");
              }}
            >
              All logs
            </MenuItem>
            <MenuItem
              icon={<NoteOutlinedIcon/>}
              onClick={() => {
                setDisplayType("standard-log");
                setStandardLogType("status");
              }}
            >
              Status
            </MenuItem>
            <MenuItem
              icon={<NoteOutlinedIcon />}
              onClick={() => {
                setDisplayType("standard-log");
                setStandardLogType("mime-type");
              }}
            >
              Mimetype
            </MenuItem>
          </SubMenu>
          <SubMenu icon={<SsidChartOutlinedIcon />} label="Graphs">
            <MenuItem
              icon={<SearchOutlinedIcon />}
              onClick={() => {
                setGraph(graphtype);
                setDisplayType("graph");
              }}
            >
              <TextField
                size="small"
                value={graphtype}
                onChange={(e) => {
                  setGraphType(e.target.value);
                }}
              ></TextField>
            </MenuItem>
          </SubMenu>

          <SubMenu icon={<FindInPageOutlinedIcon />} label="Raw logs">
            <MenuItem icon={<SearchOutlinedIcon />}
            onClick={() => {
              setRawLog(rawlogtype);
              setDisplayType("raw-log");
            }}
            >
              <TextField
                size="small"
                value={rawlogtype}
                onChange={(e) => {
                  setRawLogType(e.target.value);
                }}
              ></TextField>
            </MenuItem>
          </SubMenu>
        </Menu>
      </Sidebar>
    </div>
  );
}

export default SideBar;
