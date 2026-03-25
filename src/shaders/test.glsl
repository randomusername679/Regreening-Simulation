#version 330

out float value;
out float product;

void main() {
    value = gl_VertexID;
    product = gl_VertexID * gl_VertexID;
}
