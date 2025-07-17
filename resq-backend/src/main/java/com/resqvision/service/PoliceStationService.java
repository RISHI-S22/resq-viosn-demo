package com.resqvision.service;

import com.resqvision.model.PoliceStation;
import com.resqvision.repository.PoliceStationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PoliceStationService {

    @Autowired
    private PoliceStationRepository policeStationRepository;

    public List<PoliceStation> getAllPoliceStations() {
        return policeStationRepository.findAll();
    }

    public PoliceStation addPoliceStation(PoliceStation policeStation) {
        return policeStationRepository.save(policeStation);
    }
}
