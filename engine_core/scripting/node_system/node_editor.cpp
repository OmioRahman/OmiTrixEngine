#include "node_editor.hpp"
#include <imgui.h>
#include <vector>

struct Node {
    int id;
    std::string title;
    ImVec2 position;
};

std::vector<Node> nodes;

void DrawNode(Node& node) {
    ImGui::SetCursorScreenPos(node.position);
    ImGui::BeginGroup();
    ImGui::Text("%s", node.title.c_str());
    ImGui::EndGroup();
    ImGui::SetCursorScreenPos(node.position);
    ImGui::InvisibleButton("node", ImVec2(100, 100));
}

void RenderNodeEditor() {
    ImGui::Begin("Node Editor");
    for (auto& node : nodes) {
        DrawNode(node);
    }
    ImGui::End();
}