import 'package:flutter/foundation.dart';
import '../models/user.dart';
import '../services/mock_data_service.dart';

class AuthController extends ChangeNotifier {
  AppUser? _user;
  bool _isLoading = false;

  AppUser? get user => _user;
  bool get isLoading => _isLoading;
  bool get isSignedIn => _user != null;

  Future<void> signIn(String email, String password) async {
    _isLoading = true;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 800));
    _user = MockDataService.currentUser();
    _isLoading = false;
    notifyListeners();
  }

  Future<void> signOut() async {
    _user = null;
    notifyListeners();
  }
}