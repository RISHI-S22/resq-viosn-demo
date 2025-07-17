package com.resqvision.service;

import com.resqvision.model.Accident;
import com.resqvision.repository.AccidentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class AccidentService {
    @Autowired
    private AccidentRepository accidentRepository;

    public Accident saveAccident(Accident accident) {
        return accidentRepository.save(accident);
    }

    public List<Accident> getAllAccidents() {
        return accidentRepository.findAll();
    }

    public Optional<Accident> getAccidentById(Long id) {
        return accidentRepository.findById(id);
    }
}
