import 'package:intl/intl.dart';

String formatCompactNumber(num value) {
  return NumberFormat.compact().format(value);
}

String formatMoney(num value) {
  return NumberFormat.compactCurrency(symbol: '\$').format(value);
}

String formatShortDate(String iso) {
  final dt = DateTime.tryParse(iso);
  if (dt == null) return '';
  return DateFormat('MMM d').format(dt);
}
