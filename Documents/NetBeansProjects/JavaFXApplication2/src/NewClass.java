/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import javafx.application.Application ;
import static javafx.application.Application.launch;
import javafx.event.ActionEvent ; 
import javafx.event.EventHandler ;
import javafx.scene.Scene ; 
import javafx.scene.control.Button ;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane ; 
import javafx.scene.layout.VBox;
import javafx.stage.Stage ; 
        

/**
 *
 * @author Ghimire
 */
public class NewClass extends Application {
    Button button ; 
    Stage  window ; 
   public static void main(String[] args) {
      
         launch(args); 
    }
    @Override
    public void start(Stage primaryStage) throws Exception{
        window = primaryStage ; 
        window.setTitle ("Title of the window") ; 
        
        HBox topMenu =  new HBox();
        Button buttonA = new Button("File");
        Button buttonB = new Button("edit");
        Button buttonC = new Button("view");
        Button buttonD = new Button("Run");
        topMenu.getChildren().addAll(buttonA, buttonB, buttonC, buttonD);
        
        
        VBox leftMenu =  new VBox();
        Button buttonE = new Button("E");
        Button buttonF = new Button("F");
        Button buttonG = new Button("G");
        Button buttonH = new Button("H");
        leftMenu.getChildren().addAll(buttonE, buttonF, buttonG, buttonH);
        
        window.setOnCloseRequest(e -> {
            e.consume(); 
            closeProgram() ;
            
                }); 
       button = new Button() ; 
       button.setText(" Close Program "); 
      
        button.setOnAction(e -> {
          closeProgram(); 
        }) ;
       // StackPane layout = new StackPane();
       // layout.getChildren().add(button);
        
        
        BorderPane borderPane = new BorderPane(); 
        borderPane.setTop(topMenu); 
        borderPane.setLeft(leftMenu);
        Scene scene = new Scene (borderPane, 300, 250) ; 
        primaryStage.setScene(scene); 
        primaryStage.show();
        
    }

    private void closeProgram(){
        Boolean answer = Confirmbox.display("title", " do you want to close ") ; 
       if(answer) 
           window.close();
    }
   

    
}
