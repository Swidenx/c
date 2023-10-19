public class Ordenamiento {
    
    public void intercambio(int vector[]){
        for (int i =0;i < vector.length;i++){
            for (int j=i+1 ; j<vector.length;j++){
                if(vector[i]>vector[j]){
                    int aux= vector[i];
                    vector[i]= vector[j];
                    vector[j]= aux;
                }

            }

            
        }
        
    }


}





public class App {
    public static void main(String[] args) throws Exception {
        int[] v = VectorUtil.generar(10);
        VectorUtil.imprimirVector(v);

        Ordenamiento ord = new Ordenamiento();
        ord.intercambio(v);
        VectorUtil.imprimirVector(v);

    }
}





import java.util.Random;

public class VectorUtil {

    public static int[] generar(int tamanio){
        Random rnd = new Random();
        
        int vector[] = new int[tamanio];
        for(int i = 0; i < tamanio; i++){
            vector[i] = rnd.nextInt(100);
        }
        return vector;
    }

    public static void imprimirVector(int vector[]){
        for(int j= 0; j < vector.length; j++){
            System.out.print(vector[j] + " ");
        }
        System.out.println();
    }
}

