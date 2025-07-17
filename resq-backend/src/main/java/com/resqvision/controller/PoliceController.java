package com.resqvision.controller;

import com.resqvision.model.PoliceStation;
import com.resqvision.service.PoliceStationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/police")
public class PoliceController {

    @Autowired
    private PoliceStationService policeStationService;

    @GetMapping
    public List<PoliceStation> getAllPoliceStations() {
        return policeStationService.getAllPoliceStations();
    }

    @PostMapping
    public PoliceStation addPoliceStation(@RequestBody PoliceStation policeStation) {
        return policeStationService.addPoliceStation(policeStation);
    }
}
