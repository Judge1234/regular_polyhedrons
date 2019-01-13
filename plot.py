from regularpolyhedrons import *
import matplotlib.pyplot as plt
import matplotlib as mpl




def generate_plot():


    SAMPLE_SIZE = 16


    label1 = 'Tetrahedron'
    label2 = 'Cube'
    label3 = 'Octahedron'
    label4 = 'Dodecahedron'
    label5 = 'Icosahedron'

    mpl.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(10, 10))

    plt.title(label='Regular Polyhedrons')
    plt.xlabel('Edge Length')
    plt.ylabel('Surface Area & Volume')
    
    plt.plot([tetrahedron_volume(i) for i in range(SAMPLE_SIZE)], 'C1', label=label1)
    plt.plot([tetrahedron_surface_area(i) for i in range(SAMPLE_SIZE)], 'C1')
    
    plt.plot([cube_volume(i) for i in range(SAMPLE_SIZE)], 'C2', label=label2)
    plt.plot([cube_surface_area(i) for i in range(SAMPLE_SIZE)], 'C2')

    plt.plot([octahedron_volume(i) for i in range(SAMPLE_SIZE)], 'C3', label=label3)
    plt.plot([octahedron_surface_area(i) for i in range(SAMPLE_SIZE)], 'C3')

    plt.plot([dodecahedron_volume(i) for i in range(SAMPLE_SIZE)], 'C4', label=label4)
    plt.plot([dodecahedron_surface_area(i) for i in range(SAMPLE_SIZE)], 'C4')

    plt.plot([icosahedron_volume(i) for i in range(SAMPLE_SIZE)], 'C5', label=label5)
    plt.plot([icosahedron_surface_area(i) for i in range(SAMPLE_SIZE)], 'C5')

    ax.legend()
    
    plt.show()


    
generate_plot()
