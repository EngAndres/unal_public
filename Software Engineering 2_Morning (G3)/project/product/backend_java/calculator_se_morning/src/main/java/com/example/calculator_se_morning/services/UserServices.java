package main.java.com.example.calculator_se_morning.services;

import main.java.com.example.calculator_se_morning.models.UserEntity;
import main.java.com.example.calculator_se_morning.repositories.UserRepository;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Service
public class UserServices {

    private UserRepository repo;
    private BCryptPasswordEncoder encoder;


    public UserServices(UserRepository repository){
        this.repo = repository;
    }

    public UserEntity register(UserDTO user){
        newUser.setName(user.nombre);
        return repo.save(user);
    }


}
