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
import javafx.geometry.Pos;
import javafx.scene.control.Button ; 
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane ;
import javafx.scene.layout.VBox ;
import javafx.stage.Modality;
/**
 *
 * @author Ghimire
 */public class Alertbox{
     public static void display(String title , String message){
         Stage window = new Stage () ; 
         window.initModality(Modality.APPLICATION_MODAL);
         window.setTitle(title);
         window.setWidth(250);
         
         Label label= new Label();
         label.setText(message); 
         Button closebutton = new Button("close the window");
         closebutton.setOnAction(e-> window.close()); 
         
         VBox layout =new VBox(10); 
         layout.getChildren().addAll(label, closebutton);
         layout.setAlignment(Pos.CENTER);
         
         Scene scene= new Scene(layout);
         window.setScene(scene) ; 
         window.showAndWait(); 
         
          
         
         
         
     }
    
}
