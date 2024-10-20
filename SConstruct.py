import os
from SCons.Script import ARGUMENTS

env = Environment(ENV=os.environ)

# Ensure MSYS2 paths are included
env.AppendENVPath('PATH', 'F:/msys64/mingw64/bin')

# Detect the build platform and target platform
build_platform = 'win' if os.name == 'nt' else 'linux'
target_platform = ARGUMENTS.get('target_platform', build_platform)

# Check for virtual environment flag and path
use_venv = ARGUMENTS.get('use_venv', 'no') == 'yes'
venv_name = ARGUMENTS.get('venv_name', 'generic_env')  # More generic name
venv_path = ARGUMENTS.get('venv_path', '/path/to/venv')  # Default path

# Paths for different platforms
if target_platform == 'win':
    if build_platform == 'linux':
        # Set cross-compilation toolchain for Windows on Linux
        env.Replace(CC='x86_64-w64-mingw32-gcc', CXX='x86_64-w64-mingw32-g++')
    python_include = 'F:/msys64/mingw64/include/python3.11'
    python_lib = 'F:/msys64/mingw64/lib'
else:
    if use_venv and os.path.exists(os.path.join(venv_path, venv_name)):
        venv = os.path.join(venv_path, venv_name)
        python_include = os.path.join(venv, 'include')
        python_lib = os.path.join(venv, 'lib')
    else:
        python_include = '/usr/local/include/python3.11'
        python_lib = '/usr/local/lib'
#  Ensure that bin dir exists
if not os.path.exists('bin'):
    os.makedirs('bin')

# Function to run CMake
def cmake_build(directory):
    build_dir = os.path.join(directory, 'build')
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    os.system(f'cd {build_dir} && cmake .. && cmake --build .')

# Build third-party libraries
third_party_dirs = [
    'third_party/bgfx',
    'third_party/jolt',
    'third_party/imgui',
    'third_party/soloud',
    'third_party/tinyxml2',
    'third_party/assimp',
    'third_party/box2dlite',
    'third_party/physfs',
    'third_party/bx'
]
for dir in third_party_dirs:
    cmake_build(dir)

# Include directories
env.Append(CPPPATH=[
    'third_party/bgfx/include',
    'third_party/jolt/include',
    'third_party/imgui',
    'third_party/soloud/include',
    'third_party/tinyxml2/include',
    'third_party/assimp/include',
    'third_party/box2dlite/include',
    'third_party/bx/include',
    'third_party/stb',
    'third_party/physfs/include',
    'include',
    python_include
])

# Link directories for libraries built by CMake
env.Append(LIBPATH=[
    'third_party/bgfx/build',
    'third_party/jolt/build',
    'third_party/imgui/build',
    'third_party/soloud/build',
    'third_party/tinyxml2/build',
    'third_party/assimp/build',
    'third_party/box2dlite/build',
    'third_party/physfs/build',
    'third_party/bx/build',
    python_lib
])

# Source files
sources = Glob('src/*.cpp') + Glob('scripts/**/*.cpp')

# Combine all sources
all_sources = sources

# Build executable
env.Program(target='bin/OmiTrix', source=all_sources)

# Ensure Python is linked correctly
env.Append(LIBS=['python3.11'])

# Note for Users
print("Ensure the Python and MSYS2 paths are set correctly for your system.")
print("Windows example: F:/msys64")
print("Linux example: /usr/local or activate virtual environment")

if use_venv:
    print(f"Building with virtual environment located at {venv_path}/{venv_name}.")
else:
    print("Building with system Python.")

if target_platform == 'win':
    print("Building for Windows.")
else:
    print("Building for Linux.")
