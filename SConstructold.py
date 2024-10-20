import os

env = Environment()
# Ensure MSYS2 paths are included
# Note: Set the paths to where Python and MSYS2 are installed on your PC.
# Example: If installed on drive F, as shown below.
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
    'third_party/physfs/',
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
    'F:\msys64\mingw64\include\python3.11'
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
    'F:/msys64/mingw64/lib'
])

# Source files
sources = Glob('src/*.cpp') + Glob('scripts/**/*.cpp')

# Combine all sources
all_sources = sources

# Build executable
env.Program(target='OmiTrix', source=all_sources)

# Ensure Python is linked correctly
env.Append(LIBS=['python3.11'])

# Python include and library path for mingw64
env.Append(CPPPATH=['F:/msys64/mingw64/include/python3.11'])
env.Append(LIBPATH=['F:/msys64/mingw64/lib'])