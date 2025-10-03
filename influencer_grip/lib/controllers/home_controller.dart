import 'package:flutter/foundation.dart';
import '../models/influencer.dart';
import '../models/campaign.dart';
import '../services/mock_data_service.dart';

class HomeController extends ChangeNotifier {
  HomeController() {
    loadHomeData();
  }

  final List<String> _categories = const [
    'All',
    'Tech',
    'Lifestyle',
    'Beauty',
    'Gaming',
    'Fitness',
  ];
  String _selectedCategory = 'All';

  List<String> get categories => _categories;
  String get selectedCategory => _selectedCategory;

  List<InfluencerProfile> _influencers = const [];
  List<Campaign> _campaigns = const [];

  List<InfluencerProfile> get influencers => _selectedCategory == 'All'
      ? _influencers
      : _influencers
          .where((i) => i.categories.contains(_selectedCategory))
          .toList(growable: false);

  List<Campaign> get campaigns => _campaigns;

  Future<void> loadHomeData() async {
    await Future<void>.delayed(const Duration(milliseconds: 200));
    _influencers = MockDataService.influencers(count: 14);
    _campaigns = MockDataService.campaigns(count: 6);
    notifyListeners();
  }

  void selectCategory(String category) {
    _selectedCategory = category;
    notifyListeners();
  }
}
