/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import javafx.application.Application ;
import javafx.event.ActionEvent ; 
import javafx.event.EventHandler ;
import javafx.geometry.Insets;
import javafx.scene.Scene ; 
import javafx.scene.control.Button ;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane ; 
import javafx.scene.layout.VBox;
import javafx.stage.Stage ; 
        

/**
 *
 * @author Ghimire
 */
public class Main extends Application {
    Button button ; 
    Stage  window ; 
   public static void main(String[] args) {
      
         launch(args); 
    }
    @Override
    public void start(Stage primaryStage) throws Exception{
        window = primaryStage ; 
        window.setTitle ("Title of the window") ; 
        
        TextField nameinput = new TextField(); 
        button = new Button("CLick");
        button.setOnAction(e-> isInt(nameinput, nameinput.getText())) ;
        
        
        VBox layout = new VBox(10 ); 
        layout.setPadding(new Insets(20,20,20,20));
        layout.getChildren().addAll(nameinput , button);
       
        /*
        GridPane grid = new GridPane(); 
        grid.setPadding(new Insets(10,10,10,10));
        grid.setVgap(8); 
        grid.setHgap(10);
        */
        window.setOnCloseRequest(e -> {
           // e.consume(); 
            closeProgram() ;
            
                }); 
       button = new Button() ; 
       button.setText(" Close Program "); 
      
        button.setOnAction(e -> {
          closeProgram(); 
        }) ;
       // StackPane layout = new StackPane();
       // layout.getChildren().add(button);
        
       /* 
        Label namelabel1 = new Label ("Username");
       GridPane.setConstraints(namelabel1, 0, 0 );
        
        TextField nameinput = new TextField("ramesh");
        GridPane.setConstraints(nameinput, 1, 0);
        
        
        Label passlabel1 = new Label ("Password");
       GridPane.setConstraints(passlabel1, 0, 1 );
        
        TextField passinput = new TextField();
        passinput.setPromptText("password");
       GridPane.setConstraints(nameinput, 1, 1);
        
        Button loginButton = new Button("Log in"); 
        GridPane.setConstraints(loginButton, 1, 2);
        
        grid.getChildren().addAll(namelabel1, nameinput, passlabel1, passinput, loginButton) ;
        */
        Scene scene = new Scene (layout, 300, 250) ; 
        
        
       window.setScene(scene); 
        window.show();
        
    }

    private void closeProgram(){
        Boolean answer = Confirmbox.display("title", " do you want to close ") ; 
       if(answer) 
           window.close();
    }
   
  private boolean isInt(TextField input, String message){
      try {
          int age = Integer.parseInt(input.getText());
          System.out.println("User is " + age);
          return true;
      }catch(NumberFormatException e){
          System.out.println("Error"+ message + " not a number");
          return false ; 
      }
  }
        
    
}
