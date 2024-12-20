import com.example.testing_001.model.Course;
import com.example.testing_001.service.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
 
import java.util.List;
//https://www.geeksforgeeks.org/spring-mvc-crud-with-example/
// CourseService is an interface 
// CourseServiceImpl implements CourseService
    //has @autoqired courseRepository
    //has @override all CRUD operations
@Controller
public class CourseController{

    @Autowired
    //Dependency injection of service
    private CourseService cService;

    @GetMapping("/")
    public string viewHome(Model model){
        return findPaginated(1 ,"courseName","asc",model);
    }

    @PostMapping("/save")
    public String saveCourse(@ModelAttribute("course") Course c){
        //call service save funciton
        cService.saveCourse(c);
        return "redirect:/"
    }


    @DeleteMapping("/delete/{id}")
    public String deleteCourse(@PathVariable (value="id") long id){
        //call service delete function
        this.cService.deleteCourse(id)
        return "redicrect:/"
    }

}