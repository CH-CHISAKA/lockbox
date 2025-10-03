import 'package:flutter/foundation.dart';
import '../models/influencer.dart';
import '../services/mock_data_service.dart';

class SearchController extends ChangeNotifier {
  final List<InfluencerProfile> _all = MockDataService.influencers(count: 50);
  String _query = '';

  String get query => _query;

  List<InfluencerProfile> get results {
    if (_query.isEmpty) return _all.take(20).toList();
    final lower = _query.toLowerCase();
    return _all
        .where((i) => i.name.toLowerCase().contains(lower) || i.categories.any((c) => c.toLowerCase().contains(lower)))
        .toList(growable: false);
  }

  void setQuery(String value) {
    _query = value;
    notifyListeners();
  }
}
