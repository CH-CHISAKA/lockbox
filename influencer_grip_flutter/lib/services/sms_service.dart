import 'dart:math';
import 'package:sms_advanced/sms_advanced.dart';

class SmsService {
  final SmsSender _smsSender = SmsSender();
  final Map<String, String> _otpStorage = {}; // In production, use secure storage
  final Random _random = Random();

  Future<bool> sendOtp(String phoneNumber) async {
    try {
      // Generate 6-digit OTP
      final otp = _generateOtp();

      // Store OTP temporarily (in production, use secure storage with expiration)
      _otpStorage[phoneNumber] = otp;

      // Send SMS
      final SmsMessage message = SmsMessage(
        phoneNumber,
        'Your InfluencerGrip verification code is: $otp. This code will expire in 5 minutes.',
      );

      final result = await _smsSender.sendSms(message);

      return result == 'SMS Sent';
    } catch (e) {
      print('Error sending OTP: $e');
      return false;
    }
  }

  Future<bool> verifyOtp(String phoneNumber, String otp) async {
    try {
      final storedOtp = _otpStorage[phoneNumber];

      if (storedOtp == null) {
        return false; // No OTP found for this number
      }

      if (storedOtp == otp) {
        // OTP is correct, remove it from storage
        _otpStorage.remove(phoneNumber);
        return true;
      }

      return false; // OTP doesn't match
    } catch (e) {
      print('Error verifying OTP: $e');
      return false;
    }
  }

  String _generateOtp() {
    return List.generate(6, (index) => _random.nextInt(10)).join();
  }

  // Request SMS permissions
  Future<bool> requestSmsPermission() async {
    try {
      final SmsQuery query = SmsQuery();
      // This will trigger permission request if needed
      await query.getAllSms;
      return true;
    } catch (e) {
      print('Error requesting SMS permission: $e');
      return false;
    }
  }

  // Clean up expired OTPs (call this periodically)
  void cleanupExpiredOtps() {
    // In a real app, you'd want to implement proper expiration logic
    // For now, we'll just clear all OTPs after 5 minutes
    _otpStorage.clear();
  }
}