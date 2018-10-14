package website;


import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MainController {
	
	@Autowired
	JdbcTemplate jdbcTemplate;

    @GetMapping("/greeting")
    public String greeting(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
        model.addAttribute("name", name);
        return "greeting";
    }
    
    
    @RequestMapping("/comment")
    public String comment(@RequestParam(name="comment") String comment) {
        String query = "insert into comments(date,content) values(CURRENT_TIMESTAMP,?)";
        jdbcTemplate.update(query, comment);
		return "redirect:/";
    }
    
    @RequestMapping("/display")
    public String homepage(Model model) {
    		List<Map<String, Object>> comments = jdbcTemplate.queryForList("SELECT * FROM comments");
    		System.out.println(comments);
        model.addAttribute("comments",comments);
    		return "comments_display";
    }
    
    
    //@RequestMapping("/")
}