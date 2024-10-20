#include "script_manager.hpp"
#include <Python.h>

void initialize_python() {
    Py_Initialize();
}

void finalize_python() {
    Py_Finalize();
}

void execute_python_script() {
    const char* script = "print('Hello from embedded Python!')";
    PyRun_SimpleString(script);
