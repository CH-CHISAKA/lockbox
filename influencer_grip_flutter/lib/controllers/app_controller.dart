import 'package:flutter/material.dart';
import '../models/encryption_settings.dart';
import '../models/network_device.dart';
import '../services/encryption_service.dart';
import '../services/network_service.dart';
import '../services/sms_service.dart';

class AppController extends ChangeNotifier {
  bool _serverRunning = false;
  bool _isLoading = false;
  String _currentView = 'home';
  List<NetworkDevice> _discoveredDevices = [];
  final EncryptionService _encryptionService = EncryptionService();
  final NetworkService _networkService = NetworkService();
  final SmsService _smsService = SmsService();

  // Getters
  bool get serverRunning => _serverRunning;
  bool get isLoading => _isLoading;
  String get currentView => _currentView;
  List<NetworkDevice> get discoveredDevices => _discoveredDevices;

  EncryptionSettings get encryptionSettings => _encryptionService.settings;
  ServerSettings get serverSettings => _networkService.serverSettings;

  // Server control methods
  Future<void> startServer() async {
    if (_serverRunning) return;

    _isLoading = true;
    notifyListeners();

    try {
      await _networkService.startServer();
      _serverRunning = true;
      notifyListeners();
    } catch (e) {
      debugPrint('Error starting server: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> stopServer() async {
    if (!_serverRunning) return;

    _isLoading = true;
    notifyListeners();

    try {
      await _networkService.stopServer();
      _serverRunning = false;
      notifyListeners();
    } catch (e) {
      debugPrint('Error stopping server: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  // Network discovery
  Future<void> discoverDevices() async {
    _isLoading = true;
    notifyListeners();

    try {
      _discoveredDevices = await _networkService.discoverDevices();
      notifyListeners();
    } catch (e) {
      debugPrint('Error discovering devices: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  // View navigation
  void navigateToView(String view) {
    _currentView = view;
    notifyListeners();
  }

  // Encryption methods
  String encryptMessage(String message, String key) {
    return _encryptionService.encrypt(message, key);
  }

  String decryptMessage(String encryptedMessage, String key) {
    return _encryptionService.decrypt(encryptedMessage, key);
  }

  // SMS methods
  Future<bool> sendOtp(String phoneNumber) async {
    return await _smsService.sendOtp(phoneNumber);
  }

  Future<bool> verifyOtp(String phoneNumber, String otp) async {
    return await _smsService.verifyOtp(phoneNumber, otp);
  }

  @override
  void dispose() {
    _networkService.dispose();
    super.dispose();
  }
}