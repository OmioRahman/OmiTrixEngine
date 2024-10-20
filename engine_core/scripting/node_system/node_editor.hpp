#pragma once

#include <imgui.h>
#include <vector>
#include <string>

// Node structure
struct Node {
    int id;
    std::string title;
    ImVec2 position;
    // Add more properties as needed
};

// Functions to manage the node editor
void DrawNode(Node& node);
void RenderNodeEditor();
void InitializeNodes(); // Optional: initialize nodes if needed
