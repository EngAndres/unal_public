package main.java.com.example.calculator_se_morning.models;

import jakarta.persistence.*;

@Entity
@Table(name="users")
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(unique = true)
    private String username;
    
    @Column
    private String password;
    
    @Column(unique = true)
    private String email;
    
    @Column
    private String phone;
}


public class UserInputDTO {

    private String nombre;
    private String nickname;
    private String password;
    private String correo;
    private String telefonos;
}