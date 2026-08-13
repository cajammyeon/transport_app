import 'dart:io';
import 'package:csv/csv.dart';
import 'dart:convert';

Future<List<List<dynamic>>> dataRead() async {
	final dataSource = File("consolidated_timing.csv");
	final List<List<dynamic>> readData = await dataSource.openRead().transform(utf8.decoder).transform(csv.decoder).toList();
	return readData;
}
void main(List<String> arguments) async {

}