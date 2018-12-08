/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import javafx.application.Application;
import javafx.scene.Scene; 
import javafx.stage.Stage ; 
import javafx.event.EventHandler ; 
import javafx.event.ActionEvent ; 
import javafx.scene.control.Button ; 
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane ;
import javafx.scene.layout.VBox ;
/**
 *
 * @author Ghimire
 */
public class Main1 extends Application {
    Stage window ; 
    Scene scene1, scene2 ; 
    Button button1 ;
   // public static void main(String[] args) {
   //         launch(args);
   // }
    @Override
    public void start(Stage primaryStage) throws Exception {
       window = primaryStage ;
       Label label1 = new Label (" welcome to the first scene "); 
       Button button = new Button("Go to scene 2 "); 
       button.setOnAction(e -> window.setScene(scene2));
       
       VBox layout1 = new VBox(20);
       layout1.getChildren().addAll(label1,button);
       scene1 = new Scene(layout1, 200, 200); 
       
       //Button 2
       button1 = new Button("this is no bueno "); 
       button1.setOnAction(e -> window.setScene(scene1));

        //l       ayout 2 
        StackPane layout2 = new StackPane(); 
        layout2.getChildren().add(button1);
        scene2 = new Scene(layout2,600,300) ;
        
        window.setScene(scene1);
        window.setTitle("title here");
        window.show(); 
        
//throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
