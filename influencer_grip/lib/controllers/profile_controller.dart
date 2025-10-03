import 'package:flutter/foundation.dart';
import '../models/user.dart';
import '../services/mock_data_service.dart';

class ProfileController extends ChangeNotifier {
  AppUser _user = MockDataService.currentUser();
  AppUser get user => _user;

  void updateBio(String bio) {
    _user = AppUser(
      id: _user.id,
      fullName: _user.fullName,
      username: _user.username,
      avatarUrl: _user.avatarUrl,
      bio: bio,
      followers: _user.followers,
      following: _user.following,
    );
    notifyListeners();
  }
}
