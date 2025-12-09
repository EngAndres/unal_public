package main.java.com.example.calculator_se_morning.controllers;

import main.java.com.example.calculator_se_morning.models.UserEntity;
import main.java.com.example.calculator_se_morning.services.UserServices;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserServices services;

    @PostMapping("/register")
    public String register(@RequestBody UserDTO user) {
        services.register(user);
        return "User added successfully";
    }
    
}
