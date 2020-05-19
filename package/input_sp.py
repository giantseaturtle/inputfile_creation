from inputfile_creation import inputfile
class input_sp(inputfile):
    """ Generating inputfiles for single-point calculations. 
    
        Attributes:
            charge (float) define the charge of system
            multiplicity (float) define the multiplicity of system
            memory (string) requested memory for calculation
            cpu (float) requested cpu for calculation
            funtion (string) defined function for calculation
            basis_set (string) defined basis_set for calculation
            dispersion (string) enable the dispersion or not
            name (string) defined the name of inputfile
            coordinate (list or string) a list or string of molecule coordinates
    """
    def __init__(self):
        inputfile.__init__(self)
    
    def generate_sp_inputfile(self):
        """Function to generate the inputfile for single-point calculation.
        
        Args: 
            None
        
        Returns: 
            com file: inputfile for calculation
    
        """
        f = open("{}.com".format(self.name),'w')
        f.write("$RunGauss\n%NprocLinda=1\n%Mem={}gb\n%NProcshared={}\n# {}\n\nTest\n\n{},{}\n{}".format(self.memory, self.cpu, self.level, self.charge, self.multiplicity, self.coordinate))