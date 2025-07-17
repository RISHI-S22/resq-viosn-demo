package com.resqvision.controller;

import com.resqvision.model.Accident;
import com.resqvision.service.AccidentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/accidents")
@CrossOrigin(origins = "*")
public class AccidentController {
    @Autowired
    private AccidentService accidentService;

    @PostMapping
    public Accident createAccident(@RequestBody Accident accident) {
        return accidentService.saveAccident(accident);
    }

    @GetMapping
    public List<Accident> getAllAccidents() {
        return accidentService.getAllAccidents();
    }

    @GetMapping("/{id}")
    public Accident getAccidentById(@PathVariable Long id) {
        return accidentService.getAccidentById(id).orElse(null);
    }
}
