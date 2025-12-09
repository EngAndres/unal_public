package main.java.com.example.calculator_se_morning.repositories;

import org.springframework.data.repository.CrudRepository;

import main.java.com.example.calculator_se_morning.models.UserEntity;
import java.util.List;

@Repository
public interface UserRepository extends CrudRepository<UserEntity, Long> {
    
    UserEntity findByUsername(String username);

    @Query("SELECT u FROM UserEntity u WHERE u.name LIKE %:name%")
    List<UserEntity> findByName(@Param("name") String name);
}
