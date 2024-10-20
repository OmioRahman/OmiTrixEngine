#include "scripting/script_manager.hpp"

int main() {
    initialize_python();
    execute_python_script();
    finalize_python();
    return 0;
}