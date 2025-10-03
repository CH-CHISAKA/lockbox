import 'package:flutter/foundation.dart';
import '../models/campaign.dart';
import '../services/mock_data_service.dart';

class CampaignsController extends ChangeNotifier {
  List<Campaign> _campaigns = const [];
  List<Campaign> get campaigns => _campaigns;

  CampaignsController() {
    load();
  }

  Future<void> load() async {
    await Future<void>.delayed(const Duration(milliseconds: 200));
    _campaigns = MockDataService.campaigns(count: 12);
    notifyListeners();
  }
}
